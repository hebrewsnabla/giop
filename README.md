# giop
search Gaussian IOps from html

# Usage
```
python get_iop.py 7 77
```
prints the info for IOp(7/77)

# Tips
* The `Overlay*.html` is corresponding to pages in current [Gaussian 16 IOps Reference](http://gaussian.com/iops). You can replace it as you like.
* The `Overlay5.html` included in this repo has been modified, to fix a bug for IOp(5/5). If you use original html file, `5id` near `IOp(5/5)` should be modified as `id`.
