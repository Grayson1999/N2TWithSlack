## [N2T](https://github.com/jmjeon94/N2T)
위의 링크를 토대로 제작하였으며 slack 기능만을 추가하여 제작했습니다.

만일 사용을 원한다면 config.py에 
```python
SLACK=dotdict(
    KEY='slack_key'
)
```
추가하여 사용하면 됩니다.

[23.10.12]
한번에 한 개의 게시글이 올라가도록 수정