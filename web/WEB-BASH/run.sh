#! /usr/bin/env bash
service apache2 start
rm /bin/sh
ln -s /bin/bash /bin/sh
/bin/bash
