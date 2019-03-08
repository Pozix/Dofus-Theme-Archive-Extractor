### Usage:
Modify the 'theme_folder_path' and 'theme_download_path' to match your folders
##
#### This script does not:
1. Check for correct theme structure
1. Check for correct dt file structure
1. Validate file types inside the archive
1. Verify all files were extracted
1. Validate extracted files
## 
#### This script does:
1. Parse a folder for correct theme archives
1. Extract from a correct .dt file author and theme names
1. Create a .txt file with a hash as name.  
The hash is an AES ECB encoded flash's byte array from a url path
1. Extract the archive content to your Dofus' custom theme folder path
