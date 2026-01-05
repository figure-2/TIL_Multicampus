# Linux command

> 리눅스 명령어들을 정리해봅시다.

- `pwd` (print working directory)
    - 현재 작업중인 경로를 출력

- `ls`(list)
    - 현재 폴더에 있는 파일, 폴더를 출력
    - `-a`(optional) : 숨김처리된 파일, 폴더까지 출력
    -  ls -a 를 칠 경우 : ./  ../  .git/  linux.command.md  markdown.md
        -> . ~ .git : 폴더 (파란색) -> 앞에 점(.)이 붙어있으면 숨김처리

.은 상위
.. 현재폴더

- `cd` (change directory)
    - 폴더이동(내가 원하는 위치로 이동) 
    - `~` : 홈으로 이동

- `mkdir` (make directory)
    - 폴더 생성

- `touch`
    - 파일 생성

- `rm` (remove)
    - 파일 및 폴더 삭제
    - `rm`  사용하면 : 파일**만**삭제 
        (ex. rm READEME.md -> 작동O, rm test -> 작동X)
    - `-r` (optional) : 폴더삭제를 위해 입력해야하는 옵션
        ***recursion(재귀) : 폴더를 지울 건데 폴더안에 파일이나 폴더가 있으면 그것도 지우고 지우는 폴더에 또 폴더나 파일이 있으면 그것도 지우라는 의미.***