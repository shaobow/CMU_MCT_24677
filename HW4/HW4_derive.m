%%
syms s
A=[0,1;-2,-3];
B=[0,1]';
C=[3,1];
C/(s*eye(2)-A)*B
%%
syms s
A=[-4,0,-3,0,0,0;
    0,-4,0,-3,0,0;
    1,0,0,0,0,0;
    0,1,0,0,0,0;
    0,0,1,0,0,0;
    0,0,0,1,0,0];
B=[1,0,0,0,0,0;
   0,1,0,0,0,0]';
C=[1,2,4,6,3,0;
   1,-1,1,-3,0,0];
D=[0,1;0,1];
simplify(C/(s*eye(6)-A)*B+D)
%%
syms s
A=[2,0;-1,-1];
B=[1,2]';
C=[2,0];
C/(s*eye(2)-A)*B
P=[B,A*B]
%%
syms s

A=[0,1,0;
   0,0,1;
   -6,7,0];
B=[0,0,1]';
C=[-4,2,0];

A_=[0,1,0;
    7,0,1;
    -6,0,0];
B_=[0,2,-4]';
C_=[1,0,0];

G=C / (s*eye(3)-A)*B;
G_=C_/(s*eye(3)-A_)*B_;

P=[B,A*B,A^2*B];
Q=[C;C*A;C*A^2];

M_inv=[Q(1:2,:);0,0,1];
M=inv(M_inv);
A_h=M_inv*A*M;
B_h=M_inv*B;
C_h=C*M;
%%
syms s
A=[-1,4;4,-1];
B=[1,1]';
C=[1,1];
C/(s*eye(2)-A)*B;
P=[B,A*B];
%%
syms lambda1 lambda2
A=[lambda1,1,0,0,0;
   0,lambda1,0,0,0;
   0,0,lambda2,1,0;
   0,0,0,lambda2,1;
   0,0,0,0,lambda2];
B=[0,1,1,0,0]';
C=[0,1,1,0,1];
P=[B,A*B,A^2*B,A^3*B,A^4*B];
Q=[C;C*A;C*A^2;C*A^3;C*A^4];

m2=intersect(null(Q)',colspace(P)','rows')';
m1=setdiff(colspace(P)',m2','rows')';
m4=setdiff(null(Q)',m2','rows')';
m3=setdiff(sym(eye(5))',[m1,m2,m4]','rows')';
M=[m1,m2,m3,m4];
M_inv=inv(M);
A_h=M_inv*A*M;
B_h=M_inv*B;
C_h=C*M;
A_co=A_h(1:2,1:2);
B_co=B_h(1:2,:);
C_co=C_h(:,1:2);

G=C / (s*eye(5)-A)*B;
G_=C_co / (s*eye(2)-A_co)*B_co;
%%
syms kT L R J b real
syms s

A=[0,1,0;
   0,0,1;
   0,-R*b/L/J,-(R*J+L*b)/L/J];
B=[0,0,1]';
C=[kT/L/J,0,0];
G=C/(s*eye(3)-A)*B
