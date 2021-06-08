# hls.js

[原项目地址:https://github.com/video-dev/hls.js](https://github.com/video-dev/hls.js)

[破解地址:https://github.com/NiaSourceCode/hls.js](https://github.com/NiaSourceCode/hls.js)

# Debug

| 功能 | 文件名 | 函数名 |
| :--: | :--: | :--: |
| 原始ts文件加载位置 | `xhr-loader.ts` | `readystatechange()` |
| `demux`和`remux`函数调用的位置 | `transmuxer.ts` | `private transmuxUnencrypted()` |
| 默认`demux`类 | `tsdemuxer.ts` |  |
| 默认`remux`类 | `mp4-remuxer.ts` |  |
| 解封装之后流加载的位置 | `buffer-control.ts` | `protected onBufferAppending()` |