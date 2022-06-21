import dropbox;

class TransferData:
    def __init__ (self, access_token):
        self.access_token = access_token;

    def upload_file(self, file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token);
        for root, dirs, files in os.walk(file_from):
        relative_path= os.path.relpath(local_path, file_from)
        dropbox_path = os.path.join(file_to, relative_path)
        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode= writeMode('overwrite'))

def main():
    accessToken= '';
    transferData = TransferData(accessToken);

    file_from = input('Enter the path of the file needed to be transfered: ');
    file_to = input('Enter the path of the destination of the transfered file: ');

    transferData.upload_file(file_from, file_to)

    print("Your file ", file_from, " has been successfully transerfered to ", file_to);

main(
