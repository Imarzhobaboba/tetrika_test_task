# pupil = [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472]
# tutor = [1594663290, 1594663430, 1594663443, 1594666473]


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    sum = 0

    # Функция для обрезки и объединения интервалов
    def process_intervals(intervals, lesson_start, lesson_end):
        # Сначала обрежем все значения по границам урока
        processed = []
        for i in range(len(intervals)):
            if lesson_start > intervals[i]:
                intervals[i] = lesson_start
            if lesson_end < intervals[i]:
                intervals[i] = lesson_end
        
        # Соберем интервалы и проверим их валидность
        valid_intervals = []
        for i in range(0, len(intervals), 2):
            start = intervals[i]
            end = intervals[i+1]
            if start < end:
                valid_intervals.append([start, end])
        
        # Объединим пересекающиеся интервалы
        if not valid_intervals:
            return []
        
        valid_intervals.sort()
        merged = [valid_intervals[0]]
        for current in valid_intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                # Объединяем интервалы
                merged[-1] = [last[0], max(last[1], current[1])]
            else:
                merged.append(current)
        return merged

    # Обрабатываем интервалы ученика и учителя
    pupil_merged = process_intervals(pupil, lesson[0], lesson[1])
    tutor_merged = process_intervals(tutor, lesson[0], lesson[1])

    # Считаем пересечения
    for pupil_int in pupil_merged:
        for tutor_int in tutor_merged:
            start = max(pupil_int[0], tutor_int[0])
            end = min(pupil_int[1], tutor_int[1])
            if start < end:
                sum += end - start

    print(sum)
    return sum


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
