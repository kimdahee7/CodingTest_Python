-- 코드를 작성해주세요
select count(ID) AS FISH_COUNT, month(TIME) AS MONTH
from FISH_INFO
group by MONTH
order by MONTH;