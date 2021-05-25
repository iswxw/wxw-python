# 批量解析iOS系统符号表的脚本

完成系统符号表uuid的提取，存入数据库

5-19已完成
目前已经提取出来信息，并且做了数据分析，后续进行数据入db操作。

```
当前系统Version： 14.2.1 固件Version： 15D27 UUID： 2AEF604B-F264-3887-AE17-61A2E3A74E44 Arch： arm64 库的相对路径 14.2.1 (15D27)/Symbols/usr/lib/libAWDSupport.dylib
-----------------------------------------------------
当前系统Version： 14.2.1 固件Version： 15D27 UUID： 7A358BDF-8597-3C9E-97A8-191CF9D1FF7C Arch： arm64 库的相对路径 14.2.1 (15D27)/Symbols/usr/lib/libnfshared.dylib
-----------------------------------------------------
当前系统Version： 14.2.1 固件Version： 15D27 UUID： 484A9352-ADEA-39E5-A632-5D438855ABB9 Arch： arm64 库的相对路径 14.2.1 (15D27)/Symbols/usr/lib/libexslt.dylib
-----------------------------------------------------
当前系统Version： 14.2.1 固件Version： 15D27 UUID： 775E53EA-CA4D-3C36-8C40-426A9C907BDE Arch： arm64 库的相对路径 14.2.1 (15D27)/Symbols/usr/lib/libassertion_launchd.dylib
```