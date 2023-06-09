ANSI_SEQ = "\x1b[$value$m"
FG_RGB = "38;2;$r$;$g$;$b$"
BG_RGB = "48;2;$r$;$g$;$b$"
END = ANSI_SEQ.replace("$value$", '0')