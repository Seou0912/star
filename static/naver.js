// 네이버 로그인 버튼 클릭
function loginWithNaver() {
  $.ajax({
    url: "/login/getNaverAuthUrl",
    type: "get",
  }).done(function (res) {
    location.href = res;
  });
}
