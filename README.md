## color-format

Make your text colorful with colorama and cf.

---

### How to use

!! - !

!c:_letter_ - color (B - black, R - red, g - green, y - yellow, b - blue, m - magenta, c - cyan, w - white, r - reset)

*   Case sensitive
*   Use `^` instead of `:` to get a light variant

!b:_letter_ - background

*   Same as color

!e:_letter_ - effect (b - bright (bold), d - dim, n - normal, r - reset **all**, u - underline, i - italic)

*   Not case sensitive
*   Only `:` supported, `^` variant isn't available
*   Colorama doesn't have `u` and `i`

Example: `!c:R!e:bAmogus!e:r`

---

### Some examples

```python
import cf
print(cf.format('!c:RHello World!!!e:r'))
# Red “Hello World!”
```

```python
[print([__import__('cf').format(input('To format: ')), __import__('os').system('cls')][0]), input()]
# Format input
```
