-- 코드를 입력하세요
SELECT YEAR(B.SALES_DATE) AS YEAR, MONTH(B.SALES_DATE) AS MONTH, A.GENDER, COUNT(DISTINCT(A.USER_ID)) AS USERS
FROM USER_INFO AS A, ONLINE_SALE AS B
WHERE A.USER_ID	= B.USER_ID	AND GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER	