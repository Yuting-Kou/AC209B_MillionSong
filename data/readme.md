Due to the large size of the data (5GB of zip file), we do not synchronize it on the github. Instead, we choose to put the data in the local version while synchronize the scripts.

Remember to keep the data under the following version:

    
    ├── AC209B_MillionSong 
        ├── data           <- the folder contains all the data
        │   ├── songs  <- the folder contains the unzip files from "Songs.zip"
        │   │   ├── ignite_talks   <- AC297r Ignite presentations
        │   │   ├── ...
        │   │   └──     
        ├── src           <- the folder contains all the script
        │   ├── EDA    <- Preprocessing and eda analysis
