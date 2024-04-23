# star
<img width="1545" alt="Screenshot 2024-04-15 at 6 35 00 PM" src="https://github.com/Seou0912/star/assets/151927766/df9c9cd9-aa36-49b4-815a-1143fad5dda2">

# 목차
#### 1. [프로젝트 개요](#프로젝트-개요)
#### 2. [기술 스택](#기술-스택)
#### 3. [주요 기능](#주요-기능)
#### 4. [화면 구성](#화면-구성)
#### 5. [팀 정보](#팀-정보)

# 프로젝트 개요
>#### 프로젝트 명
>오늘의 한마디
>
>#### 개발 기간
>2024.04.09 - 2024.04.23
>
>#### 프로젝트 소개
>생년월일을 기반으로 한 개인 맞춤형 운세를 제공하여 더욱 정확하고  
 의미 있는 정보를 얻을 수 있어요
> <b>오늘의 한마디로 시작하는 기분좋은 하루</b><br>
>OpenAi를 이용하여 띠별운세, 별자리운세, MBTI운세를 제공해주는 어플리케이션입니다.
>
# 기술 스택

#### Back End
\![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
<br>

#### Infra
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"> <img src="https://img.shields.io/badge/amazonec2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white"> <img src="https://img.shields.io/badge/jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white">
<br>

# 주요 기능

### 여행 그룹 성향 입력 및 분석 
여행 그룹의 성향을 입력받고 이를 빅데이터 기반으로 분석합니다.<br>

>#### 입력 여행 성향: <br>
>`공항`, `식도락 여행`, `쇼핑`, `제주의 문화유산`, <br>
>`레저와 체험`,`전시와 행사`, `천천히 걷기`, `휴식과 치유 여행` <br>

### 여행 지점들의 일자별 최적 동선 제공

사용자가 원하는 여행 지점들을 입력받고 거리정보, <br>
알고리즘을 기반으로 최적의 동선을 제공합니다. <br>

### 현재 여행 그룹의 여행지 추천

형태소 분석 및 빅데이터 기반으로 여행 그룹에 맞는 <br>
여행지들을 추천합니다.<br>

# 화면 구성

### 1) 로그인 및 메인페이지

<table>
  <tbody>
    <tr>
      <td>
        로그인
      </td>
      <td>
        메인 화면 
      </td>
    <tr/>
    <tr>
      <td>
      <p align="center">
      <img src="/images/로그인.gif" width="260" height="450">
      </p>
      </td>
      <td>
      <p align="center">
      <img src="/images/메인화면.gif" width="260" height="450">
      </p>
      </td>
    <tr/>
  </tobdy>
</table>

### 2) 여행 일정 정보 입력

<table>
  <tbody>
    <tr>
      <td>
        여행 제목, 기간 설정
      </td>
      <td>
        가고 싶은 여행지 추가
      </td>
    <tr/>
    <tr>
      <td>
      <p align="center">
        <img src="/images/여행일정설정.gif" width="260" height="450"  >
        </p>
      </td>
      <td>
      <p align="center">
        <img src="/images/여행지 추가.gif" width="260" height="450"  >
        </p>
      </td>
    <tr/>
  </tobdy>
</table>

### 3) 여행 일정별 추천 및 동선 제공

<table>
  <tbody>
    <tr>
      <td>
        일자별 여행 동선 제공
      </td>
      <td>
        여행 상세 동선 확인
      </td>
      <td>
        여행 상세 동선 제공
      </td>
    <tr/>
    <tr>
      <td>
      <p align="center">
        <img src="/images/여행지 자동 추천.gif" width="260" height="450"  >
        </p>
      </td>
      <td>
      <p align="center">
              <img src="/images/여행 계획보기.gif" width="260" height="450"  >
        </p>
      </td>
      <td>
      <p align="center">
      <img src="/images/지도사용법.gif" width="260" height="450"  >
        </p>
      </td>
    <tr/>
  </tobdy>
</table>

### 4) 여행 지점들의 네이버맵, 티맵 연동

<table>
  <tbody>
    <tr>
      <td>
        네이버 맵
      </td>
      <td>
        티맵 
      </td>
    <tr/>
    <tr>
      <td>
      <p align="center">
        <img src="/images/네이버맵 연동.gif" width="260" height="450"  >
        </p>
      </td>
      <td>
      <p align="center">
        <img src="/images/티맵연동.gif" width="260" height="450"  >
        </p>
      </td>
    <tr/>
  </tobdy>
</table>

### 5) 여행 그룹 성향 입력 및 추천

<table>
  <tbody>
    <tr>
      <td>
        여행지 성향 설정
      </td>
      <td>
        여행지 추천 
      </td>
    <tr/>
    <tr>
      <td>
      <p align="center">
        <img src="/images/성향체크.gif" width="260" height="450"  >
        </p>
      </td>
      <td>
      <p align="center">
        <img src="/images/추천.gif" width="260" height="450"  >
        </p>
      </td>
    <tr/>
  </tobdy>
</table>

# 아키텍쳐
<img src="/images/SA2.png" width=80% margin="auto">

# 팀 정보
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/tjsguddl96"><img src="https://avatars.githubusercontent.com/u/58164681?v=4" width="150px;" alt=""/><br /><b>김선형</b></a> <br>BE (팀장) </b><br /></td>
      <td align="center"><a href="https://github.com/smartopens"><img src="https://avatars.githubusercontent.com/u/44837403?v=4" width="150px;" alt=""/><br /><b>김현명</b></a> <br>FE </b><br /></td>
      <td align="center"><a href="https://github.com/steve15963"><img src="https://avatars.githubusercontent.com/u/77353988?v=4" width="150px;" alt=""/><br /><b>송진현</b></a> <br>FE </b><br /></td>
    <tr/>
      <td align="center"><a href="https://github.com/chech2"><img src="https://avatars.githubusercontent.com/u/90683516?v=4" width="150px;" alt=""/><br /><b>이채림</b></a> <br>BE </b><br /></td>
      <td align="center"><a href="https://github.com/juuyoungjeon"><img src="https://avatars.githubusercontent.com/u/44489852?v=4" width="150px;" alt=""/><br /><b>전주영</b></a> <br>BE (부팀장) </b><br /></td>
      <td align="center"><a href="https://github.com/leehk77789"><img src="https://avatars.githubusercontent.com/u/96775737?v=4" width="150px;" alt=""/><br /><b>정유준</b></a> <br>BE </b><br /></td>
    </tr>
  </tbody>
</table>
