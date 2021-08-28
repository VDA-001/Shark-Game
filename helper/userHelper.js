//registering user
export const signup = (user) => {
  const {email,username} = user;
  return fetch(`http://127.0.0.1:8000/api/user/register?username=${username}&email=${email}`, {
    method: "GET",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      return response.json();
    })
    .catch((err) => console.log(err));
};