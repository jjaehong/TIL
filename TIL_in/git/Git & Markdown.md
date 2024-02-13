# 승재홍의 TIL
## 2023-07-12 : 고생의 시작
- 반 배정이 된 오늘은 1일 1프로젝트가 아닌 진짜 공부를 배웠다. 점심먹고 터덜터덜 교실으로 돌아가던 중 처음으로 집가고 싶다는 생각이 들었다. 조금 지친거 같아.. 잘 쉬어주고 다시 회복해서 정진하자.. 꿈을 잊진 않았잖아? 파이팅!!

- 주요 내용으로는 마크다운 문법 및 활용, CLI 개념, Git에 대해 배웠고 

### 2. Markdown 공부 내용
- markdown : 주로 개발자들이 텍스트와 코드를 작성해 문서화하기 위해 사용함.

    2-1 링크 & 이미지 불러오기
```python
print("ninano")
```
[google로 들어가기](www.google.com)
![이미지](https://t1.daumcdn.net/cfile/tistory/117A8433516D5BF70E)
![이미지](이미지/wolf.avif)

    2-2 글씨 문법
**굵게**

*기울임*

~~취소선~~

본문
---
본문

|name|sex|age|job|
|:--:|:--:|:--:|:--:|
|Seung|M|27|student|
|Son|M|32|football|


### 3. Git 공부내용
- Git : 분산 버전 관리 시스템, 코드의 '변경 이력'을 기록하고 '협업'을 원활하게 하는 도구
- Working Directory : 실제 작업 중인 파일들이 위치하는 영역
- Staging Area : working directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
- Repository : **버전(commit)** 이력과 파일들이 영구적으로 저장되는 영역, 모든 **버전(commit)**과 변경 이력이 기록됨.

- Commit : 버전, 변경된 파일들을 저장하는 행위, 마치 사진을 찍듯이 기록한다함.
![이미지](이미지/git.png)


# gitlab

- 나의 주소를 클론 복사하고 새폴더 vscode에 git clone 사이트 주소 붙이면 생성

- 주의사항 : 하나의 repository로 올린거는 하나의 폴더로 받을 수 있다. 즉, 일대일 대응만이 가능하다.


# Github 
- one of the 원격 저장소 서비스s
1. git remote add origin URL => 로컬저장소에 원격 저장소 주소 추가, origin은 추가 원격저장소 별칭임

- git remote -v : 원격 저장소 목록 확인

![이미지](gitgitig.PNG)  
- git push -u origin master : 원격 저장소에 commit 목록을 올림(업로드)
- git pull origin master : 원격 저장소의 변경사항만을 받아옴(업데이트)
- git clone URL: 원격 저장소 전체를 복제(다운로드, 처음 다운할 때)

- gitignore : git에서 특정파일이나 디렉토리를 추적하지 않도록 설정하는 데 사용되는 txt파일(추적을 무시함, 공유하지 않아야 하는 것들에 활용)
ⓐ .gitignore 파일 생성
ⓑ gitignore에 추적원치않는 파일 작성
ⓒ git init, git status

- 팀플 도중 git 병합 충돌 : 서로 수정한 것들을 push 먼저해서 발생. 따라서 pull을 먼저 사용하고 push를 사용 해야한다!

그럼에도, 서로 관련 기록이 없는 이질적인 두 프로젝트를 병합해줄 때
- git pull origin master --allow unrelated histories


Git 커밋 정보

소스 코드 변경 내용과 함께 작성자의 이름과 이메일도 포함
문제 상황이나 코드 리뷰시 중요한 정보
Git 사용 환경 설정 도구(명령어)

git config —global user.name “(본인 이름)”
git config —global user.email “(싸피에서 등록된 이메일)”
Git 커밋 메시지

다른 개발자의 작업 내역이나 변경사항을 파악하는데 이용
변경 이력 추적 및 문제 해결에 도움
Conventional Commits

가벼운 컨벤션으로 명확한 커밋 히스토리를 생성하기 위한 간단한 규칙 제공
커밋 메시지에 신규 기능 추가, 문제 수정, 커다란 변화가 있음을 기술함
커밋 메시지 구조 - 제목, 본문, 꼬리말
본문 작성 추천!! (코딩 스타일이나 간단한 수정은 예외)
Git 브랜치

독립적인 개발 공간 제공
쉽고 빠르게 브랜치를 생성하고 이동 가능
아이디어를 쉽게 시험해 볼 수 있음
브랜치 전략

쉽고 편리한 브랜치, 계획없이 만들다 보면 남용될 수 있음
가장 대표적인 브랜치 전략은 gitflow
master, develop, feature, release, hotifx로 관리
Git 히스토리

레거시 코드 유지 보수에 중요
버그 발생 시점 파악 및 문제 해결 실마리 제공
git checkout {커밋 번호}
유용한 기능 - git stash

수정중인 파일이 있어서 브랜치 이동이 불가능할 경우 사용
현재 작업중인 내용을 모두 stash 공간에 쌓아줌

