create table instituicao (
   id_instituicao serial primary key,
   nome_instituicao varchar(150) not null unique,
   sigla varchar(20),
   tipo varchar(20) check (tipo in ('universidade','faculdade','escola','instituto','outro')),
   pais varchar(50) not null default 'brasil',
   estado varchar(50),
   cidade varchar(50),
   site varchar(200),
   ativa boolean not null default true
);



create table usuario (
   id_usuario serial primary key,
   nome_completo varchar(100) not null,
   email varchar(100) not null unique,
   senha varchar(255) not null,
   tipo varchar(15) check (tipo in ('aluno','professor','administrador')),
   data_cadastro date not null default current_date,
   ativo boolean not null default true,
   id_instituicao int references instituicao(id_instituicao),
   logradouro varchar(150),
   numero varchar(10),
   complemento varchar(100),
   bairro varchar(100),
   cidade_usuario varchar(100),
   estado_usuario varchar(50),
   cep varchar(9)
);
create table aluno (
   id_usuario int primary key references usuario(id_usuario),
   matricula_aluno varchar(20) not null unique,
   curso varchar(100)
);


create table professor (
   id_usuario int primary key references usuario(id_usuario),
   matricula_professor varchar(20) not null unique
);
create table administrador (
   id_usuario int primary key references usuario(id_usuario),
   nivel_permissao int not null default 1
);


create table disciplina (
   id_disciplina serial primary key,
   nome_disciplina varchar(100) not null unique
);
create table tag (
   id_tag serial primary key,
   nome_tag varchar(50) not null unique
);
create table materialdidatico (
   id_material serial primary key,
   titulo varchar(200) not null,
   descricao text,
   tipo_material varchar(15) check (tipo_material in ('apostila','video','exercicio','apresentacao','link_externo')),
   arquivo_ou_link varchar(500) not null,
   data_publicacao timestamp not null default current_timestamp,
   visibilidade varchar(10) default 'publico' check (visibilidade in ('publico','privado')),
   ativo boolean not null default true,
   id_disciplina int not null references disciplina(id_disciplina),
   id_autor int not null references usuario(id_usuario)
);






create table material_tag (
   id_material int references materialdidatico(id_material),
   id_tag int references tag(id_tag),
   primary key (id_material, id_tag)
);
create table colecao (
   id_colecao serial primary key,
   nome varchar(100) not null,
   descricao text,
   data_criacao timestamp not null default current_timestamp,
   visibilidade varchar(10) default 'publica' check (visibilidade in ('publica','privada')),
   ativa boolean not null default true,
   id_usuario_criador int not null references usuario(id_usuario)
);


create table material_na_colecao (
   id_colecao int references colecao(id_colecao),
   id_material int references materialdidatico(id_material),
   data_adicao timestamp not null default current_timestamp,
   primary key (id_colecao, id_material)
);
create table avaliacaomaterial (
   id_avaliacao serial primary key,
   nota int not null check (nota between 1 and 5),
   comentario text,
   data_hora timestamp not null default current_timestamp,
   id_material int not null references materialdidatico(id_material),
   id_usuario_avaliador int not null references usuario(id_usuario),
   unique (id_material, id_usuario_avaliador)
);








create table favorito (
   id_favorito serial primary key,
   data_adicao timestamp not null default current_timestamp,
   id_usuario int not null references usuario(id_usuario),
   id_material int not null references materialdidatico(id_material),
   unique (id_usuario, id_material)
);


create table comentario (
   id_comentario serial primary key,
   texto text not null,
   data_hora timestamp not null default current_timestamp,
   id_material int not null references materialdidatico(id_material),
   id_usuario_autor int not null references usuario(id_usuario),
   id_comentario_pai int references comentario(id_comentario)
);
create table denuncia (
   id_denuncia serial primary key,
   motivo varchar(20) check (motivo in ('direitos_autorais','ofensivo','incorreto','outro')),
   descricao_detalhada text,
   data_hora timestamp not null default current_timestamp,
   status varchar(10) default 'pendente' check (status in ('pendente','aprovada','rejeitada')),
   id_material int not null references materialdidatico(id_material),
   id_usuario_denunciante int not null references usuario(id_usuario),
   unique (id_material, id_usuario_denunciante)
);
create table acessomaterial (
   id_acesso serial primary key,
   data_hora_acesso timestamp not null default current_timestamp,
   oculto_no_historico boolean not null default false,
   id_material int not null references materialdidatico(id_material),
   id_usuario int references usuario(id_usuario)
);
create table professor_disciplina (
   id_usuario int references professor(id_usuario),
   id_disciplina int references disciplina(id_disciplina),
   primary key (id_usuario, id_disciplina)
);




create table votacaoutilidade (
   id_votacao serial primary key,
   tipo_voto varchar(10) check (tipo_voto in ('util','nao_util')),
   data_hora timestamp not null default current_timestamp,
   id_material int not null references materialdidatico(id_material),
   id_usuario_votante int not null references usuario(id_usuario),
   unique (id_material, id_usuario_votante)
);






create table linkcompartilhamento (
   id_link_compartilhamento serial primary key,
   token_unico varchar(64) not null unique,
   data_geracao timestamp not null default current_timestamp,
   data_expiracao timestamp,
   ativo boolean not null default true,
   id_material int not null references materialdidatico(id_material)
);




