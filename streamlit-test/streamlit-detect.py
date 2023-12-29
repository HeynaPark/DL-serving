import streamlit as st
from PIL import Image
import torch
from torchvision import transforms, models
import time
import pandas as pd


def classify_image(model, image, topk=3):
    # 이미지 전처리
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    preprocessed_image  = transform(image).unsqueeze(0)

    model.eval()

    with torch.no_grad():
        predictions = model(preprocessed_image )

    # 예측 결과 중 가장 높은 확률을 가진 클래스를 찾습니다.
    # _, predicted_class = torch.max(predictions, 1)
        
    # 상위 k 예측 결과 출력
    topk_probabilities, topk_indices = torch.topk(predictions, topk)
    
    # 예측된 클래스 인덱스와 라벨을 반환
    predicted_classes = [(idx.item()+1, get_label(idx.item()+1), prob.item()) for idx, prob in zip(topk_indices[0], topk_probabilities[0])]

    return preprocessed_image, predicted_classes


def get_label(class_index):
    with open("imagenet_labels.txt") as f:
        labels = [line.strip() for line in f.readlines()]

    return labels[class_index]


def main():
    st.title("Pytorch와 Streamlit을 사용한 이미지 분류")

    # 이미지 업로드
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # 이미지를 열어서 분류 수행
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # ResNet 모델 로드
        model = models.resnet18(pretrained=True)
        st.write("Model: ResNet-18")

        # 이미지 분류 수행
        preprocessed_image, predicted_classes  = classify_image(model, image)

        with st.spinner("Please wait.."):
            time.sleep(2)

        # 결과를 출력
        st.subheader("Classification Result:")
        # print(predicted_classes)
        df = pd.DataFrame(predicted_classes, columns=["Class Index", "Class Label", "Probability"])
        df["Class Label"] = df["Class Label"].str.split(n=1).str[1]
        st.markdown(f"<style>table{{font-size: 18px !important;}}</style>", unsafe_allow_html=True)
        st.dataframe(df.style.highlight_max(subset="Probability"))

        # 전처리된 이미지 출력
        st.subheader("Preprocessed Image:")
        # st.image(preprocessed_image[0], caption="Preprocessed Image", use_column_width=True)
        # PyTorch 텐서를 PIL Image로 변환
        preprocessed_pil_image = transforms.ToPILImage()(preprocessed_image[0])

        # 변환된 PIL Image를 Streamlit을 사용하여 표시
        st.image(preprocessed_pil_image, caption="Preprocessed Image", use_column_width=True)
        st.balloons()

if __name__ == '__main__':
    main()
