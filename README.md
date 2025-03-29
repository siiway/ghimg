# ghimg

Cloudflare Pages 托管图床

URL: `https://ghimg.siiway.top` *(+ 文件路径)*

> [!IMPORTANT]
> 注意文件大小不能超过 **25M**

## 缓存策略

有两种情况会触发长缓存 **(6 个月)**:

1. 查询字符串包含 `enable-cache`
2. 文件扩展名为下面表达式中的一个

> [!NOTE]
> *前提条件：**查询字符串不包含 `disable-cache`***
> 缓存规则表达式如下

```
(http.host eq "ghimg.siiway.top" and http.request.uri.query contains "enable-cache" and not http.request.uri.query contains "disable-cache") or (http.host eq "ghimg.siiway.top" and http.request.uri.path.extension in {"7z" "avi" "avif" "apk" "bin" "bmp" "bz2" "class" "css" "csv" "doc" "docx" "dmg" "ejs" "eot" "eps" "exe" "flac" "gif" "gz" "ico" "iso" "jar" "jpg" "jpeg" "js" "mid" "midi" "mkv" "mp3" "mp4" "ogg" "otf" "pdf" "pict" "pls" "png" "ppt" "pptx" "ps" "rar" "svg" "svgz" "swf" "tar" "tif" "tiff" "ttf" "webm" "webp" "woff" "woff2" "xls" "xlsx" "zip" "zst"} and not http.request.uri.query contains "disable-cache")
```