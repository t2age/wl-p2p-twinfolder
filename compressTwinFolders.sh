cd build/
echo "compressing  build/twin-UNO/  to  build/twin-UNO.tar.gz"
tar  -czvf  twin-UNO.tar.gz  twin-UNO/ >/dev/null

echo "compressing  build/twin-DUO/  to  build/twin-DUO.tar.gz"
tar  -czvf  twin-DUO.tar.gz  twin-DUO/ >/dev/null

echo
echo "To unpack/extract the '.tar.gz' files, use:"
echo
echo "tar  -xzvf  twin-UNO.tar.gz"
echo "tar  -xzvf  twin-DUO.tar.gz"
echo

cd ..
