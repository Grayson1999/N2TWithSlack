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
한 번에 한 개의 게시글과 수정 요청 파일만 업로드 되게 수정

if 수정 요청 페이지 5개 and 발행 요청 페이지 3개:<br>
/t업로드 수정 요청 페이지 5 and 발행 요청 페이지 1개

※main_with_slack.py 파일에만 적용
