select count(*), ch.name from comics co
inner join characters ch on co.id = ch.id
group by ch.name