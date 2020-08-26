# coding=utf-8
# auther:wangc
# 2020-08-25

# 截取照片存储目录
path_photos_from_camera = "data/data_faces_from_camera/"

# Dlib 人脸 landmark 特征点检测器，训练好的人脸 68 点特征检测器，进行人脸面部轮廓特征提取
landmark_path = "data/data_dlib/shape_predictor_68_face_landmarks.dat"

# Dlib Resnet 人脸识别模型
resnet_path = "data/data_dlib/dlib_face_recognition_resnet_model_v1.dat"

#特征值csv文件地址
path_features_known_csv = "data/features_all.csv"