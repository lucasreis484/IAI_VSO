from pathlib import Path
import cv2
fps = 10
def imagens_para_video(
    pasta: str | Path,
    saida: str | Path,
    fps: float = 10.0,
    extensoes: set[str] = {".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".webp"},
    codec: str = "mp4v",  # mp4v, XVID, MJPG, avc1...
) -> None:
    pasta = Path(pasta)
    saida = Path(saida)

    # 1. Coletar e ordenar as imagens
    imagens = sorted(
        f for f in pasta.iterdir()
        if f.is_file() and f.suffix.lower() in extensoes
    )

    if not imagens:
        raise ValueError(f"Nenhuma imagem encontrada em {pasta}")

    print(f"Encontradas {len(imagens)} imagens")
    print(f"Primeira: {imagens[0].name}")
    print(f"Última:   {imagens[-1].name}")

    # 2. Descobrir tamanho a partir da primeira imagem
    primeira = cv2.imread(str(imagens[0]))
    if primeira is None:
        raise ValueError(f"Não foi possível ler {imagens[0]}")
    altura, largura = primeira.shape[:2]
    print(f"Resolução: {largura}x{altura}")

    # 3. Criar o writer
    fourcc = cv2.VideoWriter_fourcc(*codec)
    writer = cv2.VideoWriter(str(saida), fourcc, fps, (largura, altura))

    if not writer.isOpened():
        raise RuntimeError("Não foi possível abrir o VideoWriter. Verifique o codec.")

    # 4. Escrever cada frame
    try:
        for i, caminho in enumerate(imagens, 1):
            frame = cv2.imread(str(caminho))
            if frame is None:
                print(f"[aviso] Ignorando {caminho.name} (não pôde ser lido)")
                continue

            # Redimensiona se a imagem tiver tamanho diferente
            if frame.shape[:2] != (altura, largura):
                frame = cv2.resize(frame, (largura, altura))

            writer.write(frame)

            if i % 50 == 0 or i == len(imagens):
                print(f"  {i}/{len(imagens)}")
    finally:
        writer.release()

    print(f"Vídeo salvo em: {saida}")


if __name__ == "__main__":
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\00\image_0",
        saida="video_00.mp4",
        fps=fps,
    )
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\01\image_0",
        saida="video_01.mp4",
        fps=fps,
    )
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\02\image_0",
        saida="video_02.mp4",
        fps=fps,
    )
    
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\03\image_0",
        saida="video_03.mp4",
        fps=fps,
    )
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\04\image_0",
        saida="video_04.mp4",
        fps=fps,
    )
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\05\image_0",
        saida="video_05.mp4",
        fps=fps,
    )
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\06\image_0",
        saida="video_06.mp4",
        fps=fps,
    )
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\07\image_0",
        saida="video_07.mp4",
        fps=fps,
    )
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\08\image_0",
        saida="video_09.mp4",
        fps=fps,
    )
    
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\10\image_0",
        saida="video_10.mp4",
        fps=fps,
    )
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\11\image_0",
        saida="video_11.mp4",
        fps=fps,
    )
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\12\image_0",
        saida="video_12.mp4",
        fps=fps,
    )

    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\13\image_0",
        saida="video_13.mp4",
        fps=fps,
    )
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\14\image_0",
        saida="video_14.mp4",
        fps=fps,
    )
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\15\image_0",
        saida="video_15.mp4",
        fps=fps,
    )
    
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\16\image_0",
        saida="video_16.mp4",
        fps=fps,
    )
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\17\image_0",
        saida="video_17.mp4",
        fps=fps,
    )
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\18\image_0",
        saida="video_18.mp4",
        fps=fps,
    )
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\19\image_0",
        saida="video_19.mp4",
        fps=fps,
    )
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\20\image_0",
        saida="video_20.mp4",
        fps=fps,
    )
    imagens_para_video(
        pasta= r"C:\Users\Arthur_Publio\Desktop\Arthur_Publio\OD\BD_KITTI\data_odometry_gray\dataset\sequences\21\image_0",
        saida="video_21.mp4",
        fps=fps,
    )
    
