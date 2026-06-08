insert into instituicao (nome_instituicao, sigla, tipo, pais, estado, cidade, site, ativa) values
('universidade federal do ceara', 'ufc', 'universidade', 'brasil', 'ceara', 'fortaleza', 'www.ufc.br', true),
('universidade estadual do ceara', 'uece', 'universidade', 'brasil', 'ceara', 'fortaleza', 'www.uece.br', true),
('instituto federal do ceara', 'ifce', 'instituto', 'brasil', 'ceara', 'fortaleza', 'www.ifce.edu.br', true),
('universidade de sao paulo', 'usp', 'universidade', 'brasil', 'sao paulo', 'sao paulo', 'www.usp.br', true),
('universidade federal do rio de janeiro', 'ufrj', 'universidade', 'brasil', 'rio de janeiro', 'rio de janeiro', 'www.ufrj.br', true),
('faculdade farias brito', 'ffb', 'faculdade', 'brasil', 'ceara', 'fortaleza', 'www.fariasbrito.edu.br', true),
('universidade federal de minas gerais', 'ufmg', 'universidade', 'brasil', 'minas gerais', 'belo horizonte', 'www.ufmg.br', true),
('escola politecnica', 'poli', 'escola', 'brasil', 'ceara', 'fortaleza', 'www.poli.br', true),
('instituto de ensino superior', 'iesb', 'instituto', 'brasil', 'distrito federal', 'brasilia', 'www.iesb.br', true),
('universidade federal da bahia', 'ufba', 'universidade', 'brasil', 'bahia', 'salvador', 'www.ufba.br', true);














insert into usuario (nome_completo, email, senha, tipo, data_cadastro, ativo, id_instituicao, logradouro, numero, bairro, cidade_usuario, estado_usuario, cep) values
('joao silva', 'joao.silva@email.com', 'senha123', 'aluno', '2025-01-10', true, 1, 'rua das flores', '100', 'centro', 'fortaleza', 'ce', '60000-000'),
('maria santos', 'maria.santos@email.com', 'senha456', 'professor', '2025-01-15', true, 1, 'avenida beira mar', '500', 'meireles', 'fortaleza', 'ce', '60165-120'),
('carlos oliveira', 'carlos.oliveira@email.com', 'senha789', 'administrador', '2025-01-20', true, 2, 'rua dragao do mar', '200', 'centro', 'fortaleza', 'ce', '60060-390'),
('ana pereira', 'ana.pereira@email.com', 'senha321', 'aluno', '2025-02-01', true, 3, 'rua dos tabajaras', '150', 'aldeota', 'fortaleza', 'ce', '60150-060'),
('pedro costa', 'pedro.costa@email.com', 'senha654', 'professor', '2025-02-10', true, 1, 'avenida dom luis', '300', 'aldeota', 'fortaleza', 'ce', '60160-230'),
('fernanda lima', 'fernanda.lima@email.com', 'senha987', 'aluno', '2025-02-15', true, 4, 'rua augusta', '250', 'cerqueira cesar', 'sao paulo', 'sp', '01412-000'),
('rafael souza', 'rafael.souza@email.com', 'senha147', 'professor', '2025-03-01', true, 5, 'avenida atlantica', '1000', 'copacabana', 'rio de janeiro', 'rj', '22021-001'),
('camila rocha', 'camila.rocha@email.com', 'senha258', 'aluno', '2025-03-10', true, 2, 'rua das acacias', '75', 'boa viagem', 'fortaleza', 'ce', '60811-250'),
('lucas alves', 'lucas.alves@email.com', 'senha369', 'aluno', '2025-03-15', false, 3, 'rua santo antonio', '400', 'centro', 'fortaleza', 'ce', '60030-110'),
('beatriz martins', 'beatriz.martins@email.com', 'senha159', 'professor', '2025-03-20', true, 6, 'avenida universidade', '800', 'benfica', 'fortaleza', 'ce', '60416-200');


insert into aluno (id_usuario, matricula_aluno, curso) values
(1, '20210001', 'engenharia da computacao'),
(4, '20210002', 'sistemas de informacao'),
(6, '20210003', 'ciencia da computacao'),
(8, '20210004', 'engenharia de software'),
(9, '20210005', 'redes de computadores');






insert into professor (id_usuario, matricula_professor) values
(2, 'prof001'),
(5, 'prof002'),
(7, 'prof003'),
(10, 'prof004');
insert into administrador (id_usuario, nivel_permissao) values
(3, 3);






insert into disciplina (nome_disciplina) values
('banco de dados'),
('programacao orientada a objetos'),
('estrutura de dados'),
('engenharia de software'),
('redes de computadores'),
('inteligencia artificial'),
('desenvolvimento web'),
('sistemas operacionais'),
('calculo i'),
('algebra linear');








insert into tag (nome_tag) values
('prova'),
('exercicio'),
('videoaula'),
('resumo'),
('slide'),
('livro'),
('tutorial'),
('podcast'),
('mapamental'),
('desafio');





insert into materialdidatico (titulo, descricao, tipo_material, arquivo_ou_link, data_publicacao, visibilidade, ativo, id_disciplina, id_autor) values
('apostila de bd', 'apostila completa de banco de dados', 'apostila', '/arquivos/apostila_bd.pdf', '2025-03-01 10:00:00', 'publico', true, 1, 2),
('video aula poo', 'introducao a programacao orientada a objetos', 'video', 'https://youtube.com/video_poo', '2025-03-05 14:30:00', 'publico', true, 2, 5),
('lista de estrutura de dados', 'exercicios sobre listas e arvores', 'exercicio', '/arquivos/lista_ed.pdf', '2025-03-10 09:15:00', 'publico', true, 3, 2),
('slides engenharia', 'aula sobre metodologias ageis', 'apresentacao', '/arquivos/slides_engsoft.pdf', '2025-03-12 11:00:00', 'privado', true, 4, 7),
('tutorial redes', 'configuracao de roteadores', 'link_externo', 'https://youtube.com/tutorial_redes', '2025-03-15 16:20:00', 'publico', true, 5, 5),
('apostila ia', 'introducao a inteligencia artificial', 'apostila', '/arquivos/apostila_ia.pdf', '2025-03-18 08:45:00', 'publico', true, 6, 10),
('video web dev', 'desenvolvimento com react', 'video', 'https://vimeo.com/webdev_react', '2025-03-20 13:30:00', 'publico', true, 7, 2),
('exercicio so', 'threads e processos', 'exercicio', '/arquivos/exercicio_so.pdf', '2025-03-22 10:00:00', 'publico', true, 8, 5),
('resumo calculo', 'derivadas e integrais', 'apostila', '/arquivos/resumo_calculo.pdf', '2025-03-25 15:00:00', 'privado', false, 9, 7),
('video algebra', 'matrizes e determinantes', 'video', 'https://youtube.com/algebra_linear', '2025-03-28 12:00:00', 'publico', true, 10, 10);




insert into material_tag (id_material, id_tag) values
(1, 1), (1, 4), (1, 5),
(2, 3), (2, 4),
(3, 2), (3, 1),
(4, 5),
(5, 3), (5, 7),
(6, 4), (6, 6),
(7, 3), (7, 7),
(8, 2),
(9, 4), (9, 9),
(10, 3), (10, 10);












insert into colecao (nome, descricao, data_criacao, visibilidade, ativa, id_usuario_criador) values
('bd essentials', 'materiais essenciais de banco de dados', '2025-04-01 09:00:00', 'publica', true, 1),
('poo completo', 'curso completo de poo', '2025-04-02 10:30:00', 'privada', true, 4),
('estudos ia', 'materiais sobre inteligencia artificial', '2025-04-03 14:15:00', 'publica', true, 6),
('redes basico', 'introducao a redes', '2025-04-04 08:00:00', 'publica', true, 8),
('calculo ufu', 'materiais de calculo', '2025-04-05 11:45:00', 'publica', false, 1);






insert into material_na_colecao (id_colecao, id_material, data_adicao) values
(1, 1, '2025-04-01 09:05:00'),
(1, 8, '2025-04-01 09:10:00'),
(2, 2, '2025-04-02 10:35:00'),
(3, 6, '2025-04-03 14:20:00'),
(3, 10, '2025-04-03 14:25:00'),
(4, 5, '2025-04-04 08:05:00'),
(5, 9, '2025-04-05 11:50:00');


insert into avaliacaomaterial (nota, comentario, data_hora, id_material, id_usuario_avaliador) values
(5, 'excelente material!', '2025-04-10 10:00:00', 1, 4),
(4, 'muito bom, mas faltou exemplos', '2025-04-11 14:30:00', 1, 6),
(5, 'aula incrivel', '2025-04-12 09:15:00', 2, 1),
(3, 'conteudo basico demais', '2025-04-13 16:45:00', 2, 8),
(4, 'bons exercicios', '2025-04-14 11:00:00', 3, 1),
(5, 'recomendo', '2025-04-15 08:30:00', 4, 9),
(2, 'link quebrado', '2025-04-16 13:20:00', 5, 4),
(4, 'otimo resumo', '2025-04-17 10:45:00', 6, 8),
(5, 'melhor video sobre react', '2025-04-18 15:00:00', 7, 1),
(3, 'poderia ter mais explicacoes', '2025-04-19 12:30:00', 8, 6);




insert into favorito (data_adicao, id_usuario, id_material) values
('2025-04-10 08:00:00', 1, 2),
('2025-04-11 09:30:00', 1, 3),
('2025-04-12 10:15:00', 4, 1),
('2025-04-13 14:00:00', 6, 6),
('2025-04-14 11:45:00', 8, 5),
('2025-04-15 16:20:00', 1, 7),
('2025-04-16 13:10:00', 9, 4),
('2025-04-17 09:00:00', 4, 8),
('2025-04-18 17:30:00', 6, 2),
('2025-04-19 08:45:00', 8, 1);






insert into comentario (texto, data_hora, id_material, id_usuario_autor, id_comentario_pai) values
('otimo material, me ajudou muito', '2025-04-20 10:00:00', 1, 4, null),
('concordo com o colega', '2025-04-20 11:30:00', 1, 6, 1),
('gostaria de mais exemplos', '2025-04-21 09:15:00', 2, 1, null),
('obrigado por compartilhar', '2025-04-22 14:45:00', 3, 8, null),
('muito util', '2025-04-23 08:30:00', 4, 9, null),
('parabens pelo conteudo', '2025-04-24 16:00:00', 5, 4, null),
('excelente explicacao', '2025-04-25 10:45:00', 6, 1, null),
('recomendo a todos', '2025-04-26 13:20:00', 7, 6, null),
('poderia ser mais completo', '2025-04-27 11:00:00', 8, 8, null),
('adorei a abordagem', '2025-04-28 15:30:00', 1, 9, null);




insert into denuncia (motivo, descricao_detalhada, data_hora, status, id_material, id_usuario_denunciante) values
('direitos_autorais', 'material copiado de outro site sem autorizacao', '2025-04-15 09:00:00', 'aprovada', 5, 1),
('ofensivo', 'comentario ofensivo no material', '2025-04-16 10:30:00', 'rejeitada', 2, 4),
('incorreto', 'informacoes tecnicas incorretas', '2025-04-17 14:15:00', 'pendente', 8, 6),
('outro', 'link nao funciona mais', '2025-04-18 11:00:00', 'pendente', 5, 8),
('direitos_autorais', 'utilizacao de imagens sem credito', '2025-04-19 16:45:00', 'aprovada', 3, 1),
('ofensivo', 'conteudo improprio para estudantes', '2025-04-20 09:30:00', 'pendente', 7, 4),
('incorreto', 'formula matematica errada', '2025-04-21 13:00:00', 'rejeitada', 10, 6),
('outro', 'arquivo corrompido', '2025-04-22 10:15:00', 'pendente', 4, 8),
('direitos_autorais', 'violacao de direitos autorais', '2025-04-23 15:30:00', 'aprovada', 1, 9),
('incorreto', 'conceitos desatualizados', '2025-04-24 12:00:00', 'pendente', 6, 1);
insert into acessomaterial (data_hora_acesso, oculto_no_historico, id_material, id_usuario) values
('2025-05-01 08:00:00', false, 1, 1),
('2025-05-01 09:30:00', false, 2, 4),
('2025-05-01 10:15:00', false, 1, 6),
('2025-05-02 11:45:00', true, 3, 8),
('2025-05-02 14:00:00', false, 4, 1),
('2025-05-03 09:00:00', false, 5, 9),
('2025-05-03 16:30:00', false, 6, 4),
('2025-05-04 08:45:00', false, 2, 6),
('2025-05-04 10:20:00', false, 7, 1),
('2025-05-05 13:00:00', false, 8, 8),
('2025-05-05 15:30:00', false, 1, 9),
('2025-05-06 09:15:00', false, 9, 1),
('2025-05-06 11:00:00', false, 10, 4),
('2025-05-07 14:45:00', false, 3, 6),
('2025-05-07 16:00:00', false, 5, 8);


insert into professor_disciplina (id_usuario, id_disciplina) values
(2, 1), (2, 2), (2, 3),
(5, 4), (5, 5),
(7, 6), (7, 7),
(10, 8), (10, 9), (10, 10);




insert into votacaoutilidade (tipo_voto, data_hora, id_material, id_usuario_votante) values
('util', '2025-05-01 10:00:00', 1, 4),
('util', '2025-05-01 11:30:00', 1, 6),
('nao_util', '2025-05-02 09:15:00', 2, 1),
('util', '2025-05-02 14:45:00', 2, 8),
('util', '2025-05-03 08:30:00', 3, 1),
('nao_util', '2025-05-03 13:20:00', 3, 4),
('util', '2025-05-04 10:00:00', 4, 6),
('util', '2025-05-04 15:45:00', 5, 8),
('nao_util', '2025-05-05 09:30:00', 6, 1),
('util', '2025-05-05 16:15:00', 7, 9),
('util', '2025-05-06 11:00:00', 8, 4),
('nao_util', '2025-05-06 14:30:00', 9, 6),
('util', '2025-05-07 08:45:00', 10, 8),
('util', '2025-05-07 13:00:00', 1, 9),
('util', '2025-05-08 10:30:00', 2, 1);


insert into linkcompartilhamento (token_unico, data_geracao, data_expiracao, ativo, id_material) values
('abc123def456', '2025-05-01 09:00:00', '2025-06-01 09:00:00', true, 1),
('ghi789jkl012', '2025-05-02 10:30:00', null, true, 2),
('mno345pqr678', '2025-05-03 14:15:00', '2025-05-18 14:15:00', true, 3),
('stu901vwx234', '2025-05-04 08:00:00', '2025-06-04 08:00:00', false, 4),
('yza567bcd890', '2025-05-05 11:45:00', null, true, 5),
('efg123hij456', '2025-05-06 16:30:00', '2025-05-21 16:30:00', true, 6),
('klm789nop012', '2025-05-07 09:15:00', null, true, 7),
('qrs345tuv678', '2025-05-08 13:00:00', '2025-06-08 13:00:00', true, 8),
('wxy901zab234', '2025-05-09 10:00:00', null, true, 9),
('cde567fgh890', '2025-05-10 15:30:00', '2025-05-25 15:30:00', true, 10);

insert into usuario (nome_completo, email, senha, tipo, data_cadastro, ativo, id_instituicao, logradouro, numero, bairro, cidade_usuario, estado_usuario, cep) values
('thiago ferreira',    'thiago.ferreira@email.com',    'senha111', 'aluno',         '2025-04-01', true,  1, 'rua do sol',            '12',  'centro',         'fortaleza',      'ce', '60000-100'),
('larissa mendes',     'larissa.mendes@email.com',     'senha222', 'aluno',         '2025-04-02', true,  2, 'rua da lua',            '34',  'aldeota',        'fortaleza',      'ce', '60150-200'),
('diego carvalho',     'diego.carvalho@email.com',     'senha333', 'aluno',         '2025-04-03', true,  3, 'avenida washington',    '56',  'benfica',        'fortaleza',      'ce', '60416-100'),
('juliana nascimento', 'juliana.nascimento@email.com', 'senha444', 'aluno',         '2025-04-04', true,  4, 'rua oscar freire',      '78',  'jardins',        'sao paulo',      'sp', '01426-000'),
('vinicius araujo',    'vinicius.araujo@email.com',    'senha555', 'aluno',         '2025-04-05', true,  5, 'rua barata ribeiro',    '90',  'copacabana',     'rio de janeiro', 'rj', '22011-000'),
('patricia gomes',     'patricia.gomes@email.com',     'senha666', 'professor',     '2025-04-06', true,  1, 'rua pedro ii',          '110', 'centro',         'fortaleza',      'ce', '60000-200'),
('marcos ribeiro',     'marcos.ribeiro@email.com',     'senha777', 'professor',     '2025-04-07', true,  2, 'avenida 13 de maio',    '220', 'fatima',         'fortaleza',      'ce', '60055-100'),
('simone teixeira',    'simone.teixeira@email.com',    'senha888', 'professor',     '2025-04-08', true,  3, 'rua general sampaio',   '330', 'jacarecanga',    'fortaleza',      'ce', '60015-000'),
('roberto figueiredo', 'roberto.figueiredo@email.com', 'senha999', 'professor',     '2025-04-09', true,  6, 'rua do comercio',       '440', 'centro',         'fortaleza',      'ce', '60001-000'),
('amanda freitas',     'amanda.freitas@email.com',     'senhaAA1', 'professor',     '2025-04-10', true,  7, 'rua pampulha',          '550', 'pampulha',       'belo horizonte', 'mg', '31270-000'),
('eduardo cardoso',    'eduardo.cardoso@email.com',    'senhaAA2', 'professor',     '2025-04-11', true,  8, 'rua harmonia',          '660', 'vila madalena',  'sao paulo',      'sp', '05435-000'),
('isabela castro',     'isabela.castro@email.com',     'senhaAA3', 'administrador', '2025-04-12', true,  1, 'rua floriano',          '770', 'centro',         'fortaleza',      'ce', '60020-000'),
('henrique duarte',    'henrique.duarte@email.com',    'senhaAA4', 'administrador', '2025-04-13', true,  1, 'rua major facundo',     '880', 'centro',         'fortaleza',      'ce', '60025-000'),
('renata campos',      'renata.campos@email.com',      'senhaAA5', 'administrador', '2025-04-14', true,  2, 'rua liberato barroso',  '990', 'centro',         'fortaleza',      'ce', '60030-000'),
('gustavo moreira',    'gustavo.moreira@email.com',    'senhaAA6', 'administrador', '2025-04-15', true,  2, 'rua senador pompeu',    '111', 'centro',         'fortaleza',      'ce', '60035-000'),
('natalia borges',     'natalia.borges@email.com',     'senhaAA7', 'administrador', '2025-04-16', true,  3, 'avenida joao pessoa',   '222', 'damas',          'fortaleza',      'ce', '60115-000'),
('anderson peixoto',   'anderson.peixoto@email.com',   'senhaAA8', 'administrador', '2025-04-17', true,  3, 'rua sena madureira',    '333', 'aldeota',        'fortaleza',      'ce', '60145-000'),
('carolina azevedo',   'carolina.azevedo@email.com',   'senhaAA9', 'administrador', '2025-04-18', true,  4, 'alameda santos',        '444', 'cerqueira cesar','sao paulo',      'sp', '01419-000'),
('felipe rodrigues',   'felipe.rodrigues@email.com',   'senhaBB1', 'administrador', '2025-04-19', true,  5, 'rua visconde de piraja','555', 'ipanema',        'rio de janeiro', 'rj', '22410-000'),
('lucia monteiro',     'lucia.monteiro@email.com',     'senhaBB2', 'administrador', '2025-04-20', true,  6, 'rua nogueira acioli',   '666', 'meireles',       'fortaleza',      'ce', '60160-000');

insert into aluno (id_usuario, matricula_aluno, curso) values
(11, '20210006', 'engenharia eletrica'),
(12, '20210007', 'ciencia da computacao'),
(13, '20210008', 'sistemas de informacao'),
(14, '20210009', 'engenharia de software'),
(15, '20210010', 'matematica');

insert into professor (id_usuario, matricula_professor) values
(16, 'prof005'),
(17, 'prof006'),
(18, 'prof007'),
(19, 'prof008'),
(20, 'prof009'),
(21, 'prof010');

insert into administrador (id_usuario, nivel_permissao) values
(22, 2),
(23, 1),
(24, 1),
(25, 2),
(26, 1),
(27, 3),
(28, 1),
(29, 2),
(30, 1);

insert into colecao (nome, descricao, data_criacao, visibilidade, ativa, id_usuario_criador) values
('programacao web completo',  'materiais de html, css e javascript',        '2025-04-06 10:00:00', 'publica',  true,  6),
('ia e machine learning',     'conteudos sobre ia e aprendizado de maquina','2025-04-07 11:30:00', 'publica',  true,  1),
('sistemas operacionais',     'apostilas e videos de so',                   '2025-04-08 14:00:00', 'privada',  true,  8),
('algebra e calculo',         'materiais de matematica avancada',            '2025-04-09 09:15:00', 'publica',  true,  4),
('engenharia de software 2',  'metodologias e praticas de engenharia',      '2025-04-10 16:45:00', 'publica',  false, 6);

insert into material_na_colecao (id_colecao, id_material, data_adicao) values
(6, 7,  '2025-04-06 10:05:00'),
(7, 6,  '2025-04-07 11:35:00'),
(8, 8,  '2025-04-08 14:05:00');



insert into votacaoutilidade (tipo_voto, data_hora, id_material, id_usuario_votante) values
('util', '2025-05-10 09:00:00', 1, 1),
('util', '2025-05-11 14:30:00', 1, 8),
('util', '2025-05-12 10:15:00', 1, 9),
('nao_util', '2025-05-13 16:45:00', 1, 11),



('util', '2025-05-10 11:00:00', 2, 6),
('util', '2025-05-11 09:30:00', 2, 9),
('nao_util', '2025-05-12 15:20:00', 2, 11),


('util', '2025-05-10 08:45:00', 3, 4),
('util', '2025-05-11 13:10:00', 3, 8),
('util', '2025-05-12 10:30:00', 3, 12),

('util', '2025-05-10 14:00:00', 4, 1),
('nao_util', '2025-05-11 11:45:00', 4, 6),



('util', '2025-05-10 16:30:00', 5, 4),
('util', '2025-05-11 09:15:00', 5, 8),


('util', '2025-05-10 10:00:00', 6, 1),
('util', '2025-05-11 15:30:00', 6, 9),
('nao_util', '2025-05-12 12:00:00', 6, 11),

('util', '2025-05-10 13:45:00', 7, 4),
('util', '2025-05-11 08:30:00', 7, 6),
('util', '2025-05-12 17:15:00', 7, 12),

('util', '2025-05-10 11:30:00', 8, 1),
('nao_util', '2025-05-11 14:20:00', 8, 8),



('util', '2025-05-10 09:45:00', 9, 4),
('util', '2025-05-11 12:10:00', 9, 6),


('util', '2025-05-10 15:00:00', 10, 1),
('nao_util', '2025-05-11 10:45:00', 10, 9),
('util', '2025-05-12 16:30:00', 10, 12);


