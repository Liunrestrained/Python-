import os
import requests


class DouYin:
    def __init__(self, folder_path):
        self.folder_path = folder_path

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def download(self, file_name, url):
        res = requests.get(
            url=url,
            headers={
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS"
            }
        )
        file_path = os.path.join(self.folder_path, file_name)
        with open(file_path, mode='wb') as f:
            f.write(res.content)
            f.flush()

    def multi_download(self, video_list):
        for item in video_list:
            self.download(item[0], item[1])


if __name__ == '__main__':
    douyin_object = DouYin("videos")

    douyin_object.download(
        "罗斯.mp4",
        "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg"
    )

    video_list = [
        ("a1.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fc20000bvi413nedtlt5abaa8tg"),
        ("a2.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0d00fb60000bvi0ba63vni5gqts0uag"),
        ("a3.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")
    ]
    douyin_object.multi_download(video_list)
