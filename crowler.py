import os
import glob
import random
import shutil
from icrawler.builtin import BingImageCrawler

root_dir = "bugs_images/"
# 任意の検索したいラベルを入力
labels = ["シデムシ", "オサムシ"]
data_count = 100

def crawl_image(labels, data_count, root_dir):
    # 保存先のpath指定
    crawler = BingImageCrawler(storage={"root_dir": root_dir + "train/" + labels})
    # 保存する画像にフィルターをかける
    filters = dict(size="large", type="photo")

    crawler.crawl(keyword=labels, filters=filters, max_num=data_count)
    # test用のフォルダがすでにあったら消してなかったら作る
    if os.path.isdir(root_dir + "test/" + labels):
        shutil.rmtree(root_dir + "test/" + labels)
    os.makedirs(root_dir + "test/" + labels)
    # 移動させるべきファイルを取得
    file_list = glob.glob(root_dir + "train/*/*.jpg")
    # 移動させる割合
    test_ratio = 0.2
    # sample(対象のリスト, 数)
    test_files = random.sample(file_list, int(len(file_list) * test_ratio))

    for test_file in test_files:
        try:
            shutil.move(test_file, root_dir + "test/" + labels)
        except:
            pass


for label in labels:
    crawl_image(label, data_count, root_dir)