from __future__ import print_function
from getfilelistpy import getfilelist
from apiclient.http import MediaIoBaseDownload
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from ftplib import FTP
import pysftp
import pickle
import os.path
import httplib2
import io
import shutil

"""
    Script to donwload images from a folder in google drive, save it 
    locally and save it into a server.

    You need to get credentials from this site 
    https://developers.google.com/drive/api/v3/quickstart/python 
"""

# connect to google drive
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# ID OF GOOGLE FOLDER to add images
FOLDERS = ['1Dlfo9veYQX3YrJCYRX8EfHKcj_opQ2Rr']

server_folder = {
    full: "folder/img/ingredientes",
    partial: 'ingredientes'
}

server = {
    HOST: 'localhost',
    USER: 'user',
    PASS: 'pass'
}


def connect_to_drive():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    return (service, creds)


# connect to server  && Upload to server
def server(added=[]):
    with pysftp.Connection(host=server.HOST, username=server.USER, password=server.PASS) as sftp:
        print("Connection succesfully stablished ... ")
        sftp.chdir(server_folder.full)

        # Switch to a remote directory
        if (len(added) > 0):
            for name in added:
                edit = '.\\'+name
                if (sftp.exists(edit)):
                    if(sftp.exists(name)):
                        sftp.remove(name)
                    sftp.rename(edit, name)
        else:
            sftp.put_r(f'{server_folder.partial}', '', preserve_mtime=True)
        # Obtain structure of the remote directory '/img'


def deleteSer(added=[]):
    with pysftp.Connection(host=server.HOST, username=server.USER, password=server.PASS) as sftp:
        print("Connection succesfully stablished ... ")
        sftp.chdir(server_folder.full)

        # Switch to a remote directory
        if (len(added) > 0):
            for name in added:
                edit = '.\\'+name
                if (sftp.exists(name)):
                    sftp.remove(name)
        # Obtain structure of the remote directory '/img'

# Donwload images from drives


def download_images(drive_service, file_id, file_name):
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    fh.seek(0)

    path = f'./{server_folder.partial}/' + file_name
    with open(path, 'wb') as f:
        shutil.copyfileobj(fh, f, length=131072)
# Upload images to server


def main():
    service, creds = connect_to_drive()
    resource = {
        "oauth2": creds,
        "id": FOLDERS[1],
        "fields": "files(name,id)",
    }

    # or r = getfilelist.GetFolderTree(resource)
    res = getfilelist.GetFileList(resource)

    added = []
    items = list(res.items())
    for r in items[2][1][0]['files']:
        filename = r[u'name']
        file_id = r[u'id']
        # print(filename)
        added.append(filename)
        download_images(service, file_id, filename)  # Donwload images

    server()  # Add to folder
    deleteSer(added[1:])
    server(added=added)  # remove the weird dot


if __name__ == "__main__":
    main()
#
