import {request} from './request'

export function homeinfo() {
  return request({
    url: '/homeinfo',
    method: 'GET',
    timeout: 2000,
  })
}