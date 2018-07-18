
echo "$(cat $1)"

if [ -z "$(cat $1)" ]
then
echo "MobienceTTS(Version) is correct."
else
echo "MobienceTTS(Version) is not correct."
git pull
fi
