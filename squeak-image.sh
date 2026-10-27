#!/bin/sh
# Launch the packaged Squeak 6.1 image.
# A running image writes the image and the changes file, so the copies
# that ship under /usr are left untouched.
set -e
imgname=Squeak6.1-23976-64bit
share=/usr/share/squeak
dir=${XDG_DATA_HOME:-$HOME/.local/share}/squeak
mkdir -p "$dir"
if [ ! -e "$dir/SqueakV60.sources" ]; then
	ln -sfn "$share/SqueakV60.sources" "$dir/SqueakV60.sources"
fi
if [ $# -ge 1 ] && [ -f "$1" ]; then
	imgdir=$(dirname -- "$1")
	if [ ! -e "$imgdir/SqueakV60.sources" ]; then
		ln -sfn "$share/SqueakV60.sources" "$imgdir/SqueakV60.sources" 2>/dev/null || true
	fi
	exec /usr/bin/squeak "$@"
fi
if [ ! -e "$dir/$imgname.image" ]; then
	cp -f "$share/$imgname.image" "$dir/$imgname.image"
	cp -f "$share/$imgname.changes" "$dir/$imgname.changes"
fi
exec /usr/bin/squeak "$dir/$imgname.image" "$@"
