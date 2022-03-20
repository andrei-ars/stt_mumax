set terminal png size 800,600; set output 'freq.png';
set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 pi -1 ps 1.5;
plot 'freq.txt' using 1:2 title "f(GHz)" with linespoints ls 1;
#pause -1 "Hit any key to continue";
