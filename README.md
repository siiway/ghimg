# ghimg

Cloudflare Pages 托管图床

URL: `https://ghimg.siiway.top` *(+ 文件路径)*

> [!IMPORTANT]
> 注意文件大小不能超过 **25M**

## 文件命名格式

```ini
# 非强制
<描述>.<版本>.<扩展>
```

只需要注意 `版本` 从 1 开始，在图片内容更新后自增 1

> 默认缓存策略: `max-age=31536000` *(缓存 1 年)* <br/>
> 可以查看 `SiiWay-Cache-Control-Verify` 请求头来判断预期缓存策略

## 固定 url

如果需要固定的 url，将文件名的 `版本` 改为 `0`

> 将使用不同的缓存策略: `no-cache` *(每次确认是否更新)*