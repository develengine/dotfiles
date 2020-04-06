#!/bin/bash

to=~/dev/dotfiles

cp ~/.i3blocks.conf $to
cp ~/.config/i3/config $to
cp ~/.vimrc $to
cp ~/.config/compton.conf $to
cp ~/.bashrc $to
cp ~/apps/st/config.h $to/st
cp ~/apps/dwm/config.h $to/dwm
cp -r ~/.scripts $to
cp ~/onstart.sh $to
cp ~/dwmbar.py $to
