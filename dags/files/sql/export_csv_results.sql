COPY  (select count(*), ch."name" from characters ch inner join (select substring(substring(co.characters from '\/[0-9]*\d+''') from '\d+')::integer as result from comics co) as t on t.result = ch.id group by ch.name order by 1 desc)
TO '/tmp/final_results.csv'
DELIMITER ',' CSV HEADER;
