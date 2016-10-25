%rebase ./mysite/views/base.tpl title="DataBase - Login"


	<div class="jumbotron text-center">
	<h1>Login</h1>
	</div>
		
	<div class="row">
		<form action="/" method="post">
            Username: <input name="username" type="text" />
            <br>
            <br>
            Password: <input name="password" type="password" />
            <br>
            <br>
            <input value="Login" type="submit" />
        </form>
	</div>	