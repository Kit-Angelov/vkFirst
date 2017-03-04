#!/usr/bin/env python3
import vk
import time
import config


def auth(token):
    session = vk.AuthSession(access_token=token)
    vkapi = vk.API(session)
    return vkapi


def addFriend(vkapi):
    friend_list = vkapi.friends.getRequests()
    for attr in friend_list:
        vkapi.friends.add(user_id=attr)


def post(text, vkapi, group_id):
    get_post = vkapi.wall.get(owner_id=group_id, count=3)
    for i in range(1, 3):
        post_id = get_post[i]['id']
        vkapi.wall.createComment(owner_id=group_id, post_id=post_id, message=text)
        addFriend(vkapi)
        time.sleep(60)


if __name__ == '__main__':
    vkapi = auth(config.access_token)
    while True:
        try:
            i = 1
            for group_id in config.group_list:
                post(config.text, vkapi, group_id)
                print(i)
                i += 1
            time.sleep(300)
        except SystemError:
            time.sleep(600)
