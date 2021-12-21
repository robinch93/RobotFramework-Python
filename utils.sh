FILE=$PWD/Resources/CustomLib.py

# To comment a line in the file which contains specific keyword
comment(){
    sed -i "" -e "/$1/s/^/#/g" $FILE
}

# To uncomment a line in the file which contains specific keyword
uncomment(){
    sed -i "" -e "/$1/s/#//g" $FILE
}

open_results(){
    open -a "Google Chrome" file://$PWD/outputs/log.html
}

$*