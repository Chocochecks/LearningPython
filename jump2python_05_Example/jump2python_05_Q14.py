from operator import itemgetter

data = [('윤 서 현', 15.25),
('김 예 지', 13.31),
('박 예 원', 15.34),
('송 순 자', 15.57),
('김 시 우', 15.48),
('배 숙 자', 17.9),
('전 정 웅', 13.39),
('김 혜 진', 16.63),
('최 보 람', 17.14),
('한 지 영', 14.83),
('이 성 호', 17.7),
('김 옥 순', 16.71),
('황 민 지', 17.65),
('김 영 철', 16.7),
('주 병 철', 15.67),
('박 상 현', 14.16),
('김 영 순', 14.81),
('오 지 아', 15.13),
('윤 지 은', 16.93),
('문 재 호', 16.39)]

print(sorted(data, key=itemgetter(1)))