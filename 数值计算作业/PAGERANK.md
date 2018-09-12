create matrix A where aij = 1 / sum of nodes that node_j trusts
FOR i FROM 0 TO N DO
	if node_i not trust any nodes except itself DO
		node_i trust all nodes
	END IF
END FOR
SET 0 TO K
SET A * [1/N ....]^T to P_0
WHILE K=0 OR INF_NORM(P_K - P_(K-1)) > 0.00005 DO
	P_(K+1) = A * P_K
END WHILE
PRINT P_K