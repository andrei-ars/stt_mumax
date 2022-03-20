set terminal png size 800,600; set output 'stt2.out/mymz.png';
plot 'stt2.out/table.txt' using 1:3 title "my" with lines, 'stt2.out/table.txt' using 1:4 title "mz" with lines;
#pause -1 "Hit any key to continue";
#set output '1.png'
