Guake stores its things in (I think) ~/.gconf/apps/guake.

I'm saving settings in this module, but there isn't anything (yet) that
automatically symlinks them up.


Try:

```shell
$ ln -s ~/.carapace/bundles/interactive/70guake/gconf-guake ~/.gconf/apps/guake
```

