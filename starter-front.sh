cd front

DIR="node_modules"

if [ ! -d "$DIR" ]; then
    npm install
fi

npm run start