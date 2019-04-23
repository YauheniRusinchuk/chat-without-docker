new TypeIt('#user_is_not', {
    strings: 'Hi, it looks like you are not logged in. Login or register.',
    speed: 20,
    waitUntilVisible: true,
    afterComplete: function (instance) {
        $('.login_or_register').show('fast');
      }
});
