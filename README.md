# YouTube music downloader on Python ♥

## Installing necessary modules:
```
pip install youtube_dl pafy
```
## Running:
```
python main.py
```

#
## Main window:
<img src="readme_images/main_window.png" width=800>

## Downloading:
<img src="readme_images/downloading.png" width=800>
<img src="readme_images/music_downloaded.png" width=800>

# Errors
## Bad URL:
<img src="readme_images/bad_url.png" width=800>

> It raised when you entered not youtube site or simple text

## Module error:
<img src="readme_images/module_error.png" width=800>

> It raises because pafy module have a disadvantage with dislike count, let's fix it!

> Get that path in the running console
<img src="readme_images/module_fix_1.png" width=800>

> Go to that file
<img src="readme_images/module_fix_2.png" width=800>

> Let's see the problem, there's here in lines 53-54:
<img src="readme_images/module_fix_3.png" width=800>

> Let's correct it:
<img src="readme_images/module_fix_4.png" width=800>

```
self._likes = self._ydl_info.get('like_count', 0)
self._dislikes = self._ydl_info.get('dislike_count', 0)
```


## Save and try again :)

### Thanks for using!
