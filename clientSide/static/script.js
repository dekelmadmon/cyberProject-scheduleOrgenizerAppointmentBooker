$(".activity-text-box")

		.keyup(async ( event ) => {
		    const payload = JSON.stringify({
			        name: event.target.value,
			    });
			console.log(payload)
		    const data = await fetch("http://127.0.0.1/api/saveactivity", {
			    method: 'POST',
			    header: {'Content-Type': 'application/json'},
			    body: payload,
			})
			console.log(data)
		})
function loginPageRedirect(){
    window.location.href = "http://127.0.0.1/login"
}
function signInPageRedirect(){
    window.location.href = "http://127.0.0.1/sign-in"
}

function getValue(classname){
    return $.(classname).val()
}
$.(".submit-sign-in")
        .keyup(async (event)) => {
            const payload = JSON.stringify({
            username: $.("user-name-sign-in"),
            password: $.("password-sign-in"),
            });
            console.log(payload)
            const data = await fetch('/api/sign-in-info', {
			    method: 'POST',
			    header: {'Content-Type': 'application/json'},
			    body: payload,
        }