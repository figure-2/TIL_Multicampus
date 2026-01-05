# git 명령어

## 파일 관리

- `git init`
    - 현재 폴더에 `.git` 폴더를 생성
    - 최초로 한 번 설정
    - .git directory를 만든 것

` git add <file or folder name>` 
     - `Working Directory` 에서 `Staging Area`로 파일을 업로드(추가)함.
     - 일반적으로 모든 파일, 폴더를 추가하기 위해 아래의 코드를 사용
     - `git status`로 확인
     - `git add .` : `.`은 모든 파일과 모든 폴더를 업로드 할 때 사용
     - `git add git.md` : git.md 파일만 업로드함.(현재로는 .으로 전부 올리는게 좋음)

- `git commit -m 'message'`
    - `staging area`에 올라간 파일들의 스냅샷을 찍어 `.git directory`에 저장
    - 일반적으로 `-m` 옵션을 넣어서 커밋메세지를 추가하여 등록

- `git push origin master`
    - `master` branch를 원격저장소 `origin`으로 업로드 하는 명령어

## 설정
- `git status`
    - 현재 상태를 체크하는 명령어

- `git config`
    - git 설정을 하는 명령어
    - 일반적으로 `--global` 옵션으로 최초 한번만 실행
    - `git config --global user.email 'dudns1234@naver.com'`
        - `git config --global user.email` 를 통해 값 확인
    - `git config --global user.name 'yujin'`
        - `git config --global user.name` 를 통해 값 확인
    - 업로드할 때 누가 commit 했는지 확인하는용

- `git remote`
    - remote : 원격 저장소를 관리하는 명령어
    - `git remote add origin <remote url>`
    - <remote url>이 너무 기니까 origin이라고 부른다(별명설정)
    - 한 번만 실행
    - ` -v`(optional): remote 주소와 무슨 별명인지 확인
    - `rm origin`(optional) : remote 주소 삭제



## git 수정 내용 업로드 방법
1. 내용수정
2. ctrl + S -> 항상 저장을 하고 add를 해야함.
3. git **add** .
4. git **commit** -m '수정내용'
5. git **push** origin master