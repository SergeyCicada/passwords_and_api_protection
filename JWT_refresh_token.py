"""refresh_token
Чтобы лишний раз не тревожить пользователя, создадим ещё один токен, с большим временем жизни

1. При запросе POST на  /auth мы отдадим пару access_token и refresh_token

2. Время жизни access_token истекло

3. Клиент делает запрос PUT на /auth и обменивает свой refresh_token на новые access и refresh-токены"""