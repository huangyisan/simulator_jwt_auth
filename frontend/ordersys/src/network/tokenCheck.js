import {request} from './request'

export function tokenCheck(token) {
  return request({
    url: '/tokencheck',
    method: 'GET',
    token: token
  })
}