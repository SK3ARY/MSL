# MSL

Msl stands for `My Simple Language` (Originally was `My Small Langugage`) <br>
and was created in a single day by developer *Andrei Merryweather*. <br><br>

The language has a point which starts at a position of 0 <br>
and by using the different syntax you can move the position by indexes.

## Syntax

* `<+>` Point up
* `<->` Point down
* `<*>` Position times 2
* `</>` Position divided by 2
* `<?>` Log the current position
* `<!>` Reset position back to 0

*in MSL you can only go left to right and not up and down.

`Example Code`
```
<+> <+> <+> <+> <+> <*> <?>
```
`Output: 10`

```
<+> <+> <+> <+> <+> <*> </> <?> <!> <?>
```
`Output: 5.0 0`