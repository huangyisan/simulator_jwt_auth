import {request} from './request'

export function auth(username, password) {
  return request({
    url: '/auth',
    method: 'POST',
    data: {
      username: username,
      password: password
    }
  })
}